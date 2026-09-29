"use-client";

import { useRef, useState } from "react";

interface MicrophoneRecorderProps {
    onRecordingComplete: (audio: Blob) => void;
    disabled?: boolean;
}

export function MicrophoneRecorder({
    onRecordingComplete,
    disabled
}: MicrophoneRecorderProps) {
    const mediaRecorder = useRef<MediaRecorder | null>(null);
    const streamRef = useRef<MediaStream | null>(null);
    const chunksRef = useRef<Blob[]>([]);

    const [isRecording, setIsRecording] = useState(false);
    const [error, setError] = useState<string | null>(null);

    
}