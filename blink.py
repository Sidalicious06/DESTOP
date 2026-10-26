# ---- Control state ----

running = True
phase_active = False

import sys
import threading
from datetime import datetime

def listen_for_commands():
    global current_phase, running, phase_active, current_participant

    print("PYTHON_READY", flush=True)  # <-- Signal to main

    while running:
        line = sys.stdin.readline()
        if not line:
            break

        cmd = line.strip()

        if cmd.startswith("START"):
            # START participant phase
 
            phase_active = True
            print("LOOP STARTED")

        elif cmd.lower() == "stop":
            phase_active = False
            
            print("ACK_STOP", flush=True)

        elif cmd.lower() == "exit":
            running = False
            phase_active = False
            print("ACK_EXIT", flush=True)
            break



import cv2

# Mediapipe
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision



# scipy
from scipy.spatial import distance as dist
from scipy.spatial.transform import Rotation as R


# tools
import numpy as np
from collections import deque
import csv
import time
import threading
import os
from pathlib import Path



# INDICES # - Based on mediapipe face mesh

LEFT_EYE_INDICES = [33, 159, 158, 133, 153, 145]
RIGHT_EYE_INDICES = [362, 380, 374, 263, 386, 385]

LEFT_IRIS_INDICES = [468, 469, 470, 471, 472]
RIGHT_IRIS_INDICES = [473, 474, 475, 476, 477]

LEFT_EYELID_PUPIL_INDICES = [468, 159, 145] # Pupil, Upper Lid, Lower Lid
RIGHT_EYELID_PUPIL_INDICES = [473, 386, 374] # Pupil, Upper Lid, Lower Lid

HEAD_POSE_INDICES = [4, 152, 226, 446, 57, 287] # Nose tip, Chin, Left eye corner, Right eye corner, Left mouth corner, Right mouth corner


# Initialize MediaPipe Drawing Utils
# mp_drawing = mp.solutions.drawing_utils

# Cropping eyepatches
# def crop_eye_live(frame, landmarks, eye_indices, buffer=20):
#     if not landmarks:
#         return None

#     # Convert normalized coordinates to pixel coordinates
#     image_rows, image_cols, _ = frame.shape
#     points = []
#     for index in eye_indices:
#         point = landmarks[index]
#         # Helper function from drawing_utils to get pixel coords
#         pixel_coords = mp_drawing._normalized_to_pixel_coordinates(point.x, point.y, image_cols, image_rows)
#         if pixel_coords:
#             points.append(pixel_coords)
    
#     if not points:
#         return None

#     points = np.array(points)
#     x_min = np.min(points[:, 0])
#     x_max = np.max(points[:, 0])
#     y_min = np.min(points[:, 1])
#     y_max = np.max(points[:, 1])

#     # Apply buffer and constrain within frame boundaries
#     x_min = max(0, x_min - buffer)
#     x_max = min(image_cols, x_max + buffer)
#     y_min = max(0, y_min - buffer)
#     y_max = min(image_rows, y_max + buffer)

#     # Crop the frame
#     cropped_eye = frame[y_min:y_max, x_min:x_max]
#     return cropped_eye



import numpy as np

def crop_eye_live(frame, landmarks, eye_indices, buffer=20):
    if frame is None or landmarks is None or len(landmarks) == 0:
        return None

    image_rows, image_cols = frame.shape[:2]

    if image_rows == 0 or image_cols == 0:
        return None

    points = []

    for index in eye_indices:
        if index < 0 or index >= len(landmarks):
            continue

        point = landmarks[index]

        # Convert normalized MediaPipe coordinates to pixels.
        x = int(round(point.x * (image_cols - 1)))
        y = int(round(point.y * (image_rows - 1)))

        points.append((x, y))

    if not points:
        return None

    points = np.asarray(points, dtype=np.int32)

    # Calculate eye bounding box.
    x_min = int(points[:, 0].min()) - buffer
    x_max = int(points[:, 0].max()) + buffer + 1
    y_min = int(points[:, 1].min()) - buffer
    y_max = int(points[:, 1].max()) + buffer + 1

    # Clip to valid image boundaries.
    x_min = max(0, x_min)
    y_min = max(0, y_min)
    x_max = min(image_cols, x_max)
    y_max = min(image_rows, y_max)

    # Reject invalid or empty crops.
    if x_min >= x_max or y_min >= y_max:
        return None

    # Return Cropped Eye
    return frame[y_min:y_max, x_min:x_max].copy()



# Eyelid-pupil distances
def calculate_eyelid_pupil_distances(pupil_points):
    # Calculate MRD1 (Upper Eyelid to Pupil Center distance)
    mrd1 = dist.euclidean(pupil_points[0], pupil_points[1])
    
    # Calculate MRD2 (Lower Eyelid to Pupil Center distance)
    mrd2 = dist.euclidean(pupil_points[0], pupil_points[2])
    
    return mrd1 + mrd2

# Function to calculate EAR
def eye_aspect_ratio(eye_points):
    A = dist.euclidean(eye_points[1], eye_points[5])
    B = dist.euclidean(eye_points[2], eye_points[4])
    C = dist.euclidean(eye_points[0], eye_points[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Calculating iris diameter
def calculate_iris_diameters(iris_points):
    # iris_points should be an array of 5 points (center, top, right, bottom, left)

    # Assuming a consistent order from MediaPipe output
    center = iris_points[0]
    top = iris_points[1]
    bottom = iris_points[2]
    right = iris_points[3]
    left = iris_points[4]
    
    # Calculate vertical diameter
    vertical_diameter = dist.euclidean(top, bottom)
    
    # Calculate horizontal diameter
    horizontal_diameter = dist.euclidean(right, left)
    
    return horizontal_diameter

# Head Pose Angles
def estimate_head_pose(image_points_2d, frame_shape):
    frame_h, frame_w, _ = frame_shape
    
    # 1. Define the 3D model points (same as before)
    object_points_3d = np.float64([
        (0.0, 0.0, 0.0), (0.0, -330.0, -65.0), (-225.0, 170.0, -135.0),
        (225.0, 170.0, -135.0), (-150.0, -150.0, -125.0), (150.0, -150.0, -125.0)
    ])

    focal_length = frame_w
    cx, cy = frame_w / 2, frame_h / 2
    camera_matrix = np.array([
        [focal_length, 0, cx],
        [0, focal_length, cy],
        [0, 0, 1]
    ], dtype="double")
    dist_coeffs = np.zeros((4, 1))

    # 4. Use cv2.solvePnP
    success, rotation_vec, translation_vec = cv2.solvePnP(
        object_points_3d, image_points_2d, camera_matrix, dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE
    )

    # 5. Convert rotation vector to a rotation matrix (3x3)
    rotation_matrix, _ = cv2.Rodrigues(rotation_vec)

    # 6. Use SciPy to convert the rotation matrix to Euler angles
    # We ask for 'YXZ' convention which is often used for aviation/robotics
    # and maps well to the Pitch/Yaw/Roll you need.
    r = R.from_matrix(rotation_matrix)
    euler_angles = r.as_euler('YXZ', degrees=True) 

    yaw, pitch, roll = euler_angles 
   
    return pitch, yaw, roll

# Real Time Coordinate Extraction Helper
def coordExtract(landmarkRange, landmarks, frame):
    return np.array([(landmarks[i].x * frame.shape[1], landmarks[i].y * frame.shape[0]) 
                    for i in landmarkRange])

class EMA:
    def __init__(self, alpha=0.05):
        self.alpha = alpha
        self.value = None

    def update(self, x):
        if self.value is None:
            self.value = x
        else:
            self.value = self.alpha * x + (1 - self.alpha) * self.value

        return self.value

left_PR_ema = EMA(alpha=0.03)
right_PR_ema = EMA(alpha=0.03)

left_EAR_ema = EMA(alpha=0.03)
right_EAR_ema = EMA(alpha=0.03)





bufferLength = 5

left_PR_buffer = deque(maxlen=bufferLength)
right_PR_buffer = deque(maxlen=bufferLength)


def calculate_robust_z(current_val, buffer):
    # 1. Add current value to buffer
    buffer.append(current_val)
    
    # 2. Calculate Median (The Center)
    med = np.median(buffer)
    
    # 3. Calculate MAD (The Spread)
    # Median of |x - median|
    abs_deviation = [abs(x - med) for x in buffer]
    mad = np.median(abs_deviation)
    
    # 4. Calculate Modified Z-score
    # 0.6745 scales MAD to be consistent with Standard Deviation
    # 1e-6 prevents division by zero
    z_robust = (0.6745 * (current_val - med)) / (mad + 1e-6)
    
    return z_robust

left_ear_buffer = deque(maxlen=bufferLength)
right_ear_buffer = deque(maxlen=bufferLength)



def rolling_median_threshold(value, valueBuffer):
    # Add new value to the buffer
    valueBuffer.append(value)
    
    
    
    # Calculate the baseline (Open Eye state)
    # Using median ignores the "dips" caused by blinks
    median = np.median(valueBuffer)
    
    # Apply your K-values to find dynamic thresholds
    complete_threshold = median * 0.4
    incomplete_threshold = median * 0.6
    
    return median



def exponential_moving_avg(value, valueBuffer):

    valueBuffer.append(value)

    return


latest_data = {
    "eyeBlinkLeft": 0.0,
    "eyeBlinkRight": 0.0,
    "eyeSquintLeft": 0.0,
    "eyeSquintRight": 0.0,
    "timestamp": 0
}

data_lock = threading.Lock()


latest_frame = None
latest_left_eye_patch = None
latest_right_eye_patch = None

frame_lock = threading.Lock()



# ---- Blink detection constants ----
Z_BLINK_THRESHOLD = -3.0       # PR z-score threshold for complete blink
Z_INCOMPLETE_THRESHOLD = -2.0  # PR z-score threshold for incomplete blink
BLEND_BLINK_THRESHOLD = 0.6    # Blendshape value threshold
ANGLE_THRESHOLD = 50

EYE_CONSEC_FRAMES = 3  # Frames the blink must persist to count

# ---- State variables (global or class-level) ----
blink_counter = 0
incomplete_blink_counter = 0
blink_state = None # 'regular', 'incomplete', or None
blink_action = None # 'open', or 'active'
blink_start_time_abs = None
blink_end_time_abs = None

frame_blink_timer = 0

baseline_calibration_buffer = 150 # processed frames
buffer_count = 0

blink_start_time = None
blink_frames = []
#blink_events = []

complete_blink_max = 0
incomplete_blink_max = 0

evaluation_interval = 30 # seconds
nextTime = evaluation_interval


def result_callback(result, output_image, timestamp_ms):

    global latest_left_eye_patch, latest_right_eye_patch
    global blink_state, frame_blink_timer, blink_counter
    global incomplete_blink_counter, start_time, blink_start_time
    global blink_action, blink_frames, blink_start_time_abs
    global blink_end_time_abs, buffer_count
    global leftPR, rightPR, left_PR_baseline, right_PR_baseline
    global complete_blink_max, incomplete_blink_max
    global evaluation_interval, nextTime
    

    if not phase_active or start_time is None:
        return

    if output_image is None:
        return

    # MediaPipe Tasks output_image is RGB because that is what
    # was supplied to detect_async() in main_loop().
    frame_rgb = output_image.numpy_view()

    # Clear old patches so a missed face doesn't show stale eyes.
    left_patch = None
    right_patch = None

    if result.face_landmarks:
        landmarks = result.face_landmarks[0]

        left_patch = crop_eye_live(
            frame_rgb, landmarks, LEFT_EYE_INDICES, buffer=20
        )

        right_patch = crop_eye_live(
            frame_rgb, landmarks, RIGHT_EYE_INDICES, buffer=20
        )

    # Publish the patches together under the lock.
    with frame_lock:
        latest_left_eye_patch = left_patch
        latest_right_eye_patch = right_patch

    # Preserve the existing detection behavior when no face is found.
    if not result.face_landmarks:
        return

    # Continue with your existing blink-detection code below.
    # Replace the old variable `frame` with `frame_rgb` in the
    # remaining callback code.

    
    # result.face_landmarks is a list of detected faces

    # 1. Get Feature Input (e.g., EAR, Iris data, Pose)

    # EAR # --------------------------------------------------
    left_eye_coords = coordExtract(LEFT_EYE_INDICES, landmarks, frame_rgb)
    right_eye_coords = coordExtract(RIGHT_EYE_INDICES, landmarks, frame_rgb)

    left_ear = eye_aspect_ratio(left_eye_coords)
    right_ear = eye_aspect_ratio(right_eye_coords)
    EAR = (left_ear + right_ear) / 2.0



    # EAR Thresholds
    right_median_ear = rolling_median_threshold(left_ear, left_ear_buffer)
    left_median_ear = rolling_median_threshold(right_ear, right_ear_buffer)

    baseline_ear = (right_median_ear + left_median_ear)/2
    
        

    # IRIS # --------------------------------------------------
    left_iris_coords = coordExtract(LEFT_IRIS_INDICES, landmarks, frame_rgb)
    right_iris_coords = coordExtract(RIGHT_IRIS_INDICES, landmarks, frame_rgb)

    left_iris_diameter = calculate_iris_diameters(left_iris_coords)
    right_iris_diameter = calculate_iris_diameters(right_iris_coords)


    
    # EYELID-PUPIL DISTANCE & PR # ---------------------------------

    left_eyelid_coords = coordExtract(LEFT_EYELID_PUPIL_INDICES, landmarks, frame_rgb)
    right_eyelid_coords = coordExtract(RIGHT_EYELID_PUPIL_INDICES, landmarks, frame_rgb)

    leftIPH = calculate_eyelid_pupil_distances(left_eyelid_coords)
    rightIPH = calculate_eyelid_pupil_distances(right_eyelid_coords)

    # PR
    leftPR = (leftIPH/left_iris_diameter + 1e-6)
    rightPR = (rightIPH/right_iris_diameter + 1e-6)
    


    # Head Pose # ----------------------------------------------
    
    head_coords = coordExtract(HEAD_POSE_INDICES, landmarks, frame_rgb)
    pitch, yaw, roll = estimate_head_pose(head_coords, frame_rgb.shape)
    
    #print(f"Pose: Pitch={pitch:.1f}, Yaw={yaw:.1f}, Roll={roll:.1f}")

    # Z confidence values)
    z_l = calculate_robust_z(leftPR, left_PR_buffer)
    z_r = calculate_robust_z(rightPR, right_PR_buffer)


    #print(EAR, left_iris_diameter, left_eyelid_pupil_distance, f"Pose: Pitch={pitch:.1f}, Yaw={yaw:.1f}, Roll={roll:.1f}")

    # Blendshapes # ----------------------------------------------
    
    if result.face_blendshapes:
        face_blendshapes = result.face_blendshapes[0]
        with data_lock:
            for blendshape in face_blendshapes:
                name = blendshape.category_name
                value = blendshape.score
                if name in latest_data:
                    latest_data[name] = value
            latest_data["timestamp"] = time.time()


    left_blend_blink = latest_data["eyeBlinkLeft"]
    right_blend_blink = latest_data["eyeBlinkRight"]
    blend_blink_score = (left_blend_blink + right_blend_blink) / 2

    left_blend_squint = latest_data["eyeSquintLeft"]
    right_blend_squint = latest_data["eyeSquintRight"]
    blend_squint_score = (left_blend_squint + right_blend_squint) / 2

    # Normalization Callbacks

    global left_PR_baseline, right_PR_baseline, left_EAR_baseline, right_EAR_baseline

    # Baseline Calibration for X amount of frames
    buffer_count += 1
    
    if buffer_count < baseline_calibration_buffer:
        print("calibrating...")

        left_PR_baseline = left_PR_ema.update(leftPR)
        right_PR_baseline = right_PR_ema.update(rightPR)

        left_EAR_baseline = left_EAR_ema.update(left_median_ear)
        right_EAR_baseline = right_EAR_ema.update(right_median_ear)

        return


    left_PR_deviation = (leftPR - left_PR_baseline) / left_PR_baseline
    right_PR_deviation = (rightPR - right_PR_baseline) / right_PR_baseline

    left_EAR_deviation = (left_median_ear - left_EAR_baseline) / left_EAR_baseline
    right_EAR_deviation = (right_median_ear - right_EAR_baseline) / right_EAR_baseline

    PR_score = np.clip(
        -(left_PR_deviation + right_PR_deviation) / 2,
        0, 1
    )

    EAR_score = np.clip(
        -(left_EAR_deviation + right_EAR_deviation) / 2,
        0, 1
    )

    blink_score = (
        0.40 * PR_score +
        0.35 * EAR_score + 
        0.25 * blend_blink_score
    )

    incomplete_score = 5 * (
        0.03 * PR_score +
        0.02 * EAR_score + 
        0.25 * blend_squint_score
    )

    # ONLY UPDATE BASELINE IF BLINK IS NOT LIKELY
    
    if blink_score < 0.1:
        left_PR_baseline = left_PR_ema.update(leftPR)
        right_PR_baseline = right_PR_ema.update(rightPR)

        left_EAR_baseline = left_EAR_ema.update(left_median_ear)
        right_EAR_baseline = right_EAR_ema.update(right_median_ear)


    

   # print("Blink Score: ", blink_score, "PR: ",  PR_score, "EAR: ",  EAR_score, "Blendshape: " , blend_blink_score )
   # print("Blink Score: ", blink_score, "Incomplete Score: ",  incomplete_score)


    # Classify blink # ----------------------------------------------

    currentTime = time.time()
    elapsedTime = currentTime - start_time
    
    

    #with data_lock:
        #print({k: latest_data[k] for k in ["eyeBlinkLeft", "eyeBlinkRight", "eyeSquintLeft", "eyeSquintRight"]})
    
    #if np.abs(yaw) > ANGLE_THRESHOLD or np.abs(180 - pitch) > ANGLE_THRESHOLD or np.abs(180 - roll) > ANGLE_THRESHOLD:
     #   print("ignore, pose skew")


    both_closed = blink_score > .37
    both_incomplete = incomplete_score > .25 and both_closed == False and blink_score > .275

    if blink_score > complete_blink_max:
        complete_blink_max = blink_score

    if incomplete_score > incomplete_blink_max:
        incomplete_blink_max = incomplete_score

    
    if elapsedTime > nextTime:
        print("EVALUATE", elapsedTime)
        nextTime += evaluation_interval



    if both_closed or both_incomplete:

        if blink_state is None:
            # ---- BLINK START ----
            
            blink_state = "complete" if both_closed else "incomplete"
            
            blink_start_time = elapsedTime
            blink_start_time_abs = datetime.now().strftime('%H:%M:%S.%f')[:-3]
            blink_frames = []

        # ---- BLINK ACTIVE ----
        blink_frames.append({
            "zL": z_l,
            "zR": z_r,
            "blendL": latest_data["eyeBlinkLeft"],
            "blendR": latest_data["eyeBlinkRight"],
            "earL": left_ear,
            "earR": right_ear
        })
        

    else:
        if blink_state is not None:

            frames = blink_frames.copy()
            
            if len(frames) == 0:
                blink_state = None
                blink_start_time = None
                blink_frames = []
                return
            
            blink_end_time = elapsedTime
            duration = blink_end_time - blink_start_time

            blink_end_time_abs = datetime.now().strftime('%H:%M:%S.%f')[:-3]



            print("REPORT", complete_blink_max, incomplete_blink_max, duration, elapsedTime)


            complete_blink_max = 0
            incomplete_blink_max = 0
            

            
            

            

            blink_state = None
            blink_start_time = None
            blink_frames = []


# Locate and read mediapipe facial landmarker
    
script_dir = Path(__file__).resolve().parent

model_path = script_dir / "face_landmarker.task"

with open(model_path, 'rb') as f:
    model_data = f.read()




#Initialize options with blendshapes enabled
base_options = python.BaseOptions(model_asset_buffer=model_data)
options = mp.tasks.vision.FaceLandmarkerOptions(
    base_options=base_options,
    running_mode=mp.tasks.vision.RunningMode.LIVE_STREAM, # Correct mode for webcam
    output_face_blendshapes=True,
    result_callback=result_callback # Function MediaPipe calls asynchronously
)

detector = vision.FaceLandmarker.create_from_options(options)                


# Initialize OpenCV video capture
desired_fps = 30

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, desired_fps)

start_time = None

def main_loop():
    global running, phase_active, start_time, latest_frame

    while running:
        if not phase_active:
            time.sleep(0.01)
            continue

        if start_time is None:
            start_time = time.time()

        ret, frame = cap.read()

        if not ret:
            print("Camera read failed", flush=True)
            continue

        # Keep the original BGR frame for OpenCV display.
        with frame_lock:
            latest_frame = frame.copy()

        # Convert BGR -> RGB for MediaPipe.
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=frame_rgb
        )

        # Preserve your asynchronous landmark/blink pipeline.
        detector.detect_async(
            mp_image,
            int(time.time() * 1000)
        )

        # Copy shared references while holding the lock.
        # with frame_lock:
        #     display_frame = (
        #         latest_frame.copy()
        #         if latest_frame is not None else None
        #     )

        #     left_patch = (
        #         latest_left_eye_patch.copy()
        #         if latest_left_eye_patch is not None else None
        #     )

        #     right_patch = (
        #         latest_right_eye_patch.copy()
        #         if latest_right_eye_patch is not None else None
        #     )

        # if display_frame is not None:
        #     cv2.imshow("Webcam - BGR", display_frame)

        # if left_patch is not None and left_patch.size > 0:
        #     # Patches are RGB; convert back for OpenCV display.
        #     left_display = cv2.cvtColor(
        #         left_patch, cv2.COLOR_RGB2BGR
        #     )
        #     cv2.imshow("Left Eye Patch", left_display)
        # else:
        #     cv2.imshow(
        #         "Left Eye Patch",
        #         np.zeros((120, 240, 3), dtype=np.uint8)
        #     )

        # if right_patch is not None and right_patch.size > 0:
        #     right_display = cv2.cvtColor(
        #         right_patch, cv2.COLOR_RGB2BGR
        #     )
        #     cv2.imshow("Right Eye Patch", right_display)
        # else:
        #     cv2.imshow(
        #         "Right Eye Patch",
        #         np.zeros((120, 240, 3), dtype=np.uint8)
        #     )

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q") or key == 27:
            phase_active = False
            running = False
            break

    cap.release()
    cv2.destroyAllWindows()
    detector.close()




if __name__ == "__main__":
    threading.Thread(target=listen_for_commands, daemon=True).start()
    main_loop()

    cap.release()
    cv2.destroyAllWindows()
    detector.close()