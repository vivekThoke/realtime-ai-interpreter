const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export interface HealthResponse {
    status: string;
}

export async function getHealth(): Promise<HealthResponse> {
    const response = await fetch(`${API_URL}/health`)

    if (!response.ok) {
        throw new Error(`Health check failed: ${response.status}`);
    }

    return response.json() as Promise<HealthResponse>;
}