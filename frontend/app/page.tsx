"use client"

import { useEffect, useState } from "react";
import { getHealth } from "@/library/api";
import { HealthStatus } from "@/components/health-status";

type HealthState = "loading" | "success" | "error"; 

export default function Home() {
  const [healthState, setHealthState] = useState<HealthState>("loading");

  const [message, setMessage] = useState(
    "Checking backend connection...",
  )

  const [status, setStatus] = useState("Checking backend...");
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function checkBackend() {
      try {
        const response = await getHealth();
        
        if (response.status == "ok") {
          setHealthState("success");
          setMessage("Backend is healthy.");
          return;
        }

        setHealthState("error");
        setMessage("Backend returned an unexpected response.");
      } catch (error) {
        setHealthState("error");

        if (error instanceof Error) {
          setMessage(error.message);
        }
        else {
          setMessage("Unable to connect to the backend");
        }
      }
    }

    void checkBackend();
  }, []);

  return (
       <main className="flex min-h-screen items-center justify-center bg-gray-50 px-6">
      <section className="w-full max-w-xl rounded-2xl border bg-white p-10 shadow-sm">
        <div className="text-center">
          <h1 className="mt-2 text-3xl font-bold tracking-tight">
            Realtime AI Interpreter
          </h1>

          <p className="mt-3 text-gray-600">
            Frontend foundation and backend integration
          </p>
        </div>

        <div className="mt-8">
          <h2 className="text-sm font-semibold text-gray-900">
            Backend Status
          </h2>

          <div className="mt-3">
            <HealthStatus
              status={healthState}
              message={message}
            />
          </div>
        </div>
      </section>
    </main>
  );
}
