interface HealthStatusProps {
    status: "loading" | "success" | "error";
    message: string;
}

export function HealthStatus({
    status, 
    message
} : HealthStatusProps) {
    const statusStyles = {
        loading: "bg-gray-100 text-gray-700",
        success: "bg-green-100 text-green-700",
        error: "bg-red-100 text-red-700",
    };

    return (
        <div className={`rounded-lg px-4 py-3 text-sm font-medium ${statusStyles[status]}`}>
            {message}
        </div>
    )
}