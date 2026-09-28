import type { Language } from "@/types/language";

const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export interface HealthResponse {
    status: string;
}

export interface TranslationRequest {
  text: string;
  source_language: string;
  target_language: string;
}

export interface TranslationResponse {
  source_language: string;
  target_language: string;
  source_text: string;
  translated_text: string;
}

export class ApiError extends Error {
    status: number;

    constructor(message: string, status: number) {
        super(message);
        this.name = "ApiError";
        this.status = status;
    }
}

async function apiFetch<T>(
    endpoint: string,
    options?: RequestInit
) : Promise<T> {
    let response: Response;

    try {
        response = await fetch(`${API_URL}${endpoint}`, options);
    } catch {
        throw new ApiError(
            "Unable to connect to the backend",
            0
        );
    }

    if (!response.ok) {
        throw new ApiError(
            `Backend request failed with satus ${response.status}`,
            response.status,
        );
    }

    return response.json() as Promise<T>;
}

export async function getHealth(): Promise<HealthResponse> {
    return apiFetch<HealthResponse>("/health");
}

export function getLanguages(): Language[] {
  return [
    {
      code: "en",
      name: "English",
    },
    {
      code: "hi",
      name: "Hindi",
    },
  ];
}

export function translate(
  request: TranslationRequest,
): Promise<TranslationResponse> {
  return apiFetch<TranslationResponse>(
    "/api/v1/translate",
    {
        method: "POST",
        headers: {
        "Content-Type": "application/json",
        },
        body: JSON.stringify(request),
    },
  );
}