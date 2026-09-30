"use client"

import { useState, useMemo } from "react";

import { LanguageSelect } from "@/components/language-select";
import { TranscriptPanel } from "@/components/transcript-panel";
import { getLanguages, translate, speechToText } from "@/library/api";
import { MicrophoneRecorder } from "@/components/microphone-recorder";


export default function Home() {
  const languages = useMemo(
    () => getLanguages(),
    [],
  );

  const [sourceLanguage, setSourceLanguage] =
    useState("en");

  const [targetLanguage, setTargetLanguage] =
    useState("hi");

  const [text, setText] = useState("");

  const [transcript, setTranscript] =
    useState("");

  const [translation, setTranslation] =
    useState("");

  const [isTranslating, setIsTranslating] =
    useState(false);
  
  const [isTranscribing, setIsTranscribing] =
    useState(false);

  const [error, setError] =
    useState<string | null>(null);

  const handleTranslate = async () => {
    const trimmedText = text.trim();

    if (!trimmedText) {
      setError("Enter some text to translate.");
      return;
    }

    setError(null);
    setIsTranslating(true);

    try {
      const response = await translate({
        text: trimmedText,
        source_language: sourceLanguage,
        target_language: targetLanguage,
      });

      setTranscript(response.source_text);
      setTranslation(response.translated_text);
    } catch (error) {
      if (error instanceof Error) {
        setError(error.message);
      } else {
        setError("Translation failed.");
      }
    } finally {
      setIsTranslating(false);
    }
  };

  const handleRecordingComplete = async (
    audio: Blob,
  ) => {
    setError(null);
    setIsTranscribing(true);

    try {
      const response = await speechToText(
        audio,
        sourceLanguage,
      );

      setTranscript(response.text);
      setText(response.text);
    } catch (error) {
      if (error instanceof Error) {
        setError(error.message);
      } else {
        setError("Speech recognition failed.");
      }
    } finally {
      setIsTranscribing(false);
    }
  };

  return (
    <main className="min-h-screen bg-gray-50 px-6 py-12 text-gray-700">
      <div className="mx-auto max-w-3xl">
        <header className="text-center">
          <p className="text-sm font-medium text-gray-500">
            Sprint 1 — MVP
          </p>

          <h1 className="mt-2 text-4xl font-bold tracking-tight text-gray-900">
            Realtime AI Interpreter
          </h1>

          <p className="mt-3 text-gray-600">
            Translate spoken conversations between languages.
          </p>
        </header>

        <section className="mt-10 rounded-2xl border bg-white p-6 shadow-sm">
          <div className="grid gap-4 sm:grid-cols-2">
            <LanguageSelect
              label="From"
              value={sourceLanguage}
              options={languages}
              onChange={setSourceLanguage}
            />

            <LanguageSelect
              label="To"
              value={targetLanguage}
              options={languages}
              onChange={setTargetLanguage}
            />
          </div>

          <div className="mt-6">
            <label
              htmlFor="translation-text"
              className="text-sm font-medium text-gray-700"
            >
              Text
            </label>

            <textarea
              id="translation-text"
              value={text}
              onChange={(event) =>
                setText(event.target.value)
              }
              placeholder="Enter text to translate..."
              rows={4}
              className="mt-2 w-full resize-none rounded-lg border  border-gray-300 p-4 text-sm outline-none focus:border-gray-500"
            />
          </div>

          {error && (
            <div className="mt-4 rounded-lg bg-red-50 px-4 py-3 text-sm text-red-700">
              {error}
            </div>
          )}

          <div className="mt-6 flex justify-center">
            <button
              type="button"
              onClick={handleTranslate}
              disabled={isTranslating}
              className="rounded-full bg-gray-900 px-6 py-3 text-sm font-semibold text-gray-300 transition hover:bg-gray-700 disabled:cursor-not-allowed disabled:opacity-50"
            >
              {isTranslating
                ? "Translating..."
                : "Translate"}
            </button>
          </div>

          <div className="mt-8 space-y-6">
            <TranscriptPanel
              title="Transcript"
              text={transcript}
              emptyMessage="Your transcript will appear here."
            />

            <TranscriptPanel
              title="Translation"
              text={translation}
              emptyMessage="Your translation will appear here."
            />
          </div>

          <div className="mt-8 flex justify-center">
            <button
              type="button"
              disabled
              className="rounded-full border border-gray-300 px-6 py-3 text-sm font-semibold text-gray-500"
            >
              Start Recording
            </button>
          </div>
        </section>
      </div>
    </main>
  );
}

// export default function Home() {
//   const [healthState, setHealthState] = useState<HealthState>("loading");

//   const [message, setMessage] = useState(
//     "Checking backend connection...",
//   )
  
//   useEffect(() => {
//     async function checkBackend() {
//       try {
//         const response = await getHealth();
        
//         if (response.status == "ok") {
//           setHealthState("success");
//           setMessage("Backend is healthy.");
//           return;
//         }

//         setHealthState("error");
//         setMessage("Backend returned an unexpected response.");
//       } catch (error) {
//         setHealthState("error");

//         if (error instanceof Error) {
//           setMessage(error.message);
//         }
//         else {
//           setMessage("Unable to connect to the backend");
//         }
//       }
//     }

//     void checkBackend();
//   }, []);

//   return (
//        <main className="flex min-h-screen items-center justify-center bg-gray-50 px-6">
//       <section className="w-full max-w-xl rounded-2xl border bg-white p-10 shadow-sm">
//         <div className="text-center">
//           <h1 className="mt-2 text-3xl font-bold tracking-tight">
//             Realtime AI Interpreter
//           </h1>

//           <p className="mt-3 text-gray-600">
//             Frontend foundation and backend integration
//           </p>
//         </div>

//         <div className="mt-8">
//           <h2 className="text-sm font-semibold text-gray-900">
//             Backend Status
//           </h2>

//           <div className="mt-3">
//             <HealthStatus
//               status={healthState}
//               message={message}
//             />
//           </div>
//         </div>
//       </section>
//     </main>
//   );
// }
