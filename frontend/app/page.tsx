"use client"

import { useEffect, useState } from "react";
import { getHealth } from "@/library/api";

export default function Home() {
  const [status, setStatus] = useState("Checking backend...");
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function checkBackend() {
      try {
        const response = await getHealth();
        setStatus(response.status);
      } catch {
        setError("Unable to connect to backend.");
      }
    }

    checkBackend();
  }, []);

  return (
    <main className="flex min-h-screen items-center justify-center bg-gray-50">
      <div className="rounded-xl border bg-white p-8 text-center shadow-sm">
        <h1 className="text-3xl font-bold">
          Realtime AI Interpreter
        </h1>

        <p className="mt-4 text-gray-600">
          Sprint 0 — Frontend Foundation
        </p>

        <div className="mt-6">
          {error ? (
            <p className="text-red-600">{error}</p>
          ) : (
            <p className="text-green-600">
              Backend status: {status}
            </p>
          )}
        </div>
      </div>
    </main>
  );
}
