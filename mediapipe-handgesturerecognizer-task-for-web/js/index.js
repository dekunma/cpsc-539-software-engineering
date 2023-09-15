import {
    GestureRecognizer,
    FilesetResolver,
    DrawingUtils
  } from "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.3";

const cv = require('opencv.js');

let gestureRecognizer;
let runningMode = "VIDEO";
const createGestureRecognizer = async () => {
    const vision = await FilesetResolver.forVisionTasks(
      "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.3/wasm"
    );
    gestureRecognizer = await GestureRecognizer.createFromOptions(vision, {
      baseOptions: {
        modelAssetPath:
          // "https://storage.googleapis.com/mediapipe-models/gesture_recognizer/gesture_recognizer/float16/1/gesture_recognizer.task",
          '../assets/gesture_recognizer.task',
        delegate: "CPU"
      },
      runningMode: runningMode
    });
    demosSection.classList.remove("invisible");
  };

await createGestureRecognizer();

let cap = new cv.VideoCapture(videoSource);



let nowInMs = Date.now();
if (video.currentTime !== lastVideoTime) {
lastVideoTime = video.currentTime;
results = gestureRecognizer.recognizeForVideo(video, nowInMs);
}