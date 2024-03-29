import cv2
from ultralytics import YOLO
import random


from Training.Processing_video.IControlPoints import IControlPoints


class ControlPointsGPU(IControlPoints):
    def __init__(self, path):
        '''
        Инициализатор
        :param path: Путь к файлу с видео
        '''
        self.path = path
        self.point_pairs = [
            (5, 7), (7, 9), (11, 13), (13, 15),  # Левая и правая руки
            (5, 11), (6, 12), # Торс
            (11, 12), # Между ног
            (0, 1), (0, 2), (1, 3), (2, 4),  # Голова
            (5, 6),  # Соединение плечей
            (5, 7), (7, 9),  # Левая рука
            (6, 8), (8, 10),  # Правая рука
            (11, 13), (13, 15),  # Нога левая
            (12, 14), (14, 16)  # Нога правая
        ]

    def get_report(self) -> bool:
        '''
        Перезаписывает файл с видео (С указанием контрольных точек)
        :return: True - Если удалось, иначе Falseг
        '''

        model = YOLO('yolov8s-pose.pt')  # load a pretrained model (recommended for training)
        # Open the input video file
        cap = cv2.VideoCapture(self.path)

        if not cap.isOpened():
            raise Exception("Error: Could not open video file.")
            return False

        # Get input video frame rate and dimensions
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Define the output video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter("out.mp4", fourcc, fps, (frame_width, frame_height))

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            results = model.track(frame,  verbose=False,
                                  tracker="botsort.yaml")

            if results[0].boxes.id != None:  # this will ensure that id is not None -> exist tracks
                boxes = results[0].boxes.xyxy.cpu().numpy().astype(int)
                ids = results[0].boxes.id.cpu().numpy().astype(int)

                for box, id in zip(boxes, ids):
                    # Generate a random color for each object based on its ID
                    random.seed(int(id))
                    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                    cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3],), color, 2)
                    cv2.putText(
                        frame,
                        f"Id {id}",
                        (box[0], box[1]),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0, 255, 255),
                        2,
                    )

                for i, id in enumerate(ids):
                    keypoints = results[0].keypoints.xy[i]

                    random.seed(int(id))
                    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                    # Рисуем точки
                    for j, point in enumerate(keypoints):
                        x, y = point
                        if x > 0 and y > 0:  # Проверяем, что обе координаты больше нуля
                            cv2.circle(frame, (int(x), int(y)), 3, (0, 255, 255), -1)

                    # Соединяем точки линиями
                    for pair in self.point_pairs:
                        start, end = pair
                        if keypoints[start][0] > 0 and keypoints[start][1] > 0 and keypoints[end][0] > 0 and \
                                keypoints[end][1] > 0:  # Проверяем, что обе пары координат больше нуля
                            x1, y1 = int(keypoints[start][0]), int(keypoints[start][1])
                            x2, y2 = int(keypoints[end][0]), int(keypoints[end][1])
                            cv2.line(frame, (x1, y1), (x2, y2), color, 2)

            #cv2.imshow('MediaPipe Pose', frame)
            #if cv2.waitKey(1) & 0xFF == ord("q"):
            #    break
            out.write(frame)

        # Release the input video capture and output video writer
        cap.release()
        out.release()
        # Close all OpenCV windows
        #cv2.destroyAllWindows()
        return True



import cv2
import mediapipe as mp
from mediapipe.python.solutions.pose import PoseLandmark
from mediapipe.python.solutions.drawing_utils import DrawingSpec


class ControlPointsCPU(IControlPoints):
    def __init__(self, path):
        '''
        Инициализатор
        :param path: Путь к файлу с видео
        '''
        self.path = path
        self.mp_drawing = mp.solutions.drawing_utils
        self.drawSpecific = mp.solutions.pose
        self.mp_pose = mp.solutions.pose
        mp_drawing_styles = mp.solutions.drawing_styles

        self.custom_style = mp_drawing_styles.get_default_pose_landmarks_style()
        self.custom_connections = list(self.mp_pose.POSE_CONNECTIONS)

        # list of landmarks to exclude from the drawing
        excluded_landmarks = [
            PoseLandmark.LEFT_EYE,
            PoseLandmark.RIGHT_EYE,
            PoseLandmark.LEFT_EYE_INNER,
            PoseLandmark.RIGHT_EYE_INNER,
            PoseLandmark.LEFT_EAR,
            PoseLandmark.RIGHT_EAR,
            PoseLandmark.LEFT_EYE_OUTER,
            PoseLandmark.RIGHT_EYE_OUTER,
            PoseLandmark.NOSE,
            PoseLandmark.MOUTH_LEFT,
            PoseLandmark.MOUTH_RIGHT]


        for landmark in excluded_landmarks:
            # we change the way the excluded landmarks are drawn
            self.custom_style[landmark] = DrawingSpec(color=(0, 0, 0), thickness=0, circle_radius = 0)
            # we remove all connections which contain these landmarks
            self.custom_connections = [connection_tuple for connection_tuple in self.custom_connections
                                  if landmark.value not in connection_tuple]

    def get_report(self) -> bool:
        '''
        Перезаписывает файл с видео (С указанием контрольных точек)
        :return: True - Если удалось, иначе Falseг
        '''
        cap = cv2.VideoCapture(self.path)

        if not cap.isOpened():
            return False

        # Get input video frame rate and dimensions
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Define the output video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        path = self.path.split('.')[0]
        out = cv2.VideoWriter(path + '_out' + ".mp4", fourcc, fps, (frame_width, frame_height))

        with self.mp_pose.Pose(
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5,
                model_complexity=1) as pose:
            while True:
                ret, image = cap.read()
                if not ret:
                    break


                image.flags.writeable = False
                results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
                image.flags.writeable = True


                # Drawing the Facial Landmarks
                self.mp_drawing.draw_landmarks(
                    image,
                    results.pose_landmarks,
                    connections=self.custom_connections,  # passing the modified connections list
                    landmark_drawing_spec=self.custom_style)  # and drawing style
                #cv2.imshow('MediaPipe Pose', image)
                #if cv2.waitKey(1) & 0xFF == ord("q"):
                #    break

                out.write(image)

            # Release the input video capture and output video writer
            cap.release()
            out.release()

            # Close all OpenCV windows
            #cv2.destroyAllWindows()
        return True


if __name__ == '__main__':
    '''
    Здесь вы пишите свой код.
    Написанный код будет выполнятся только если вы ручками запускаете файлик.
    Если он импортируется то он не выполнится.
    Это сделано для того, чтобы можно было ваш метод сигментации имплиментировать в большой проект и
    функция тестирования не запускалась.
    '''
    # Load a model
    c = ControlPointsCPU("yoga2.mp4")
    res = c.get_report()
    print(res)
