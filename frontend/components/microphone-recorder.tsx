"use-client";

import { useRef, useState } from "react";

interface MicrophoneRecorderProps {
    onRecordingComplete: (audio: Blob) => void;
    disabled?: boolean;
}

export function MicrophoneRecorder({
  onRecordingComplete,
  disabled = false,
}: MicrophoneRecorderProps) {
  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const streamRef = useRef<MediaStream | null>(null);
  const chunksRef = useRef<Blob[]>([]);

  const [isRecording, setIsRecording] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const getSupportedMimeType = (): string | undefined => {
    const mimeTypes = [
      "audio/webm;codecs=opus",
      "audio/webm",
      "audio/ogg;codecs=opus",
    ];

    return mimeTypes.find((mimeType) =>
      MediaRecorder.isTypeSupported(mimeType),
    );
  };

  const startRecording = async () => {
    setError(null);

    try {
      if (!navigator.mediaDevices?.getUserMedia) {
        throw new Error(
          "Microphone access is not supported by this browser.",
        );
      }

      const stream =
        await navigator.mediaDevices.getUserMedia({
          audio: true,
        });

      const mimeType = getSupportedMimeType();

      const recorder = mimeType
        ? new MediaRecorder(stream, { mimeType })
        : new MediaRecorder(stream);

      chunksRef.current = [];

      recorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
          chunksRef.current.push(event.data);
        }
      };

      recorder.onstop = () => {
        const audioBlob = new Blob(chunksRef.current, {
          type: recorder.mimeType,
        });

        onRecordingComplete(audioBlob);

        stream.getTracks().forEach((track) => {
          track.stop();
        });

        streamRef.current = null;
        mediaRecorderRef.current = null;
      };

      streamRef.current = stream;
      mediaRecorderRef.current = recorder;

      recorder.start();
      setIsRecording(true);
    } catch (error) {
      if (error instanceof DOMException) {
        if (error.name === "NotAllowedError") {
          setError("Microphone permission was denied.");
        } else if (error.name === "NotFoundError") {
          setError("No microphone was found.");
        } else {
          setError("Unable to access the microphone.");
        }
      } else {
        setError("Unable to start recording.");
      }
    }
  };

  const stopRecording = () => {
    const recorder = mediaRecorderRef.current;

    if (!recorder || recorder.state === "inactive") {
      return;
    }

    recorder.stop();
    setIsRecording(false);
  };

  return (
    <div className="flex flex-col items-center gap-3">
      <button
        type="button"
        disabled={disabled}
        onClick={
          isRecording ? stopRecording : startRecording
        }
        className="rounded-full bg-gray-900 px-6 py-3 text-sm font-semibold text-white transition hover:bg-gray-700 disabled:cursor-not-allowed disabled:opacity-50"
      >
        {isRecording ? "Stop Recording" : "Start Recording"}
      </button>

      {isRecording && (
        <p className="text-sm text-red-600">
          Recording...
        </p>
      )}

      {error && (
        <p className="text-sm text-red-600">
          {error}
        </p>
      )}
    </div>
  );
}