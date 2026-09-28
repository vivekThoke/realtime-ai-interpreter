interface TranscriptPanelProps {
  title: string;
  text: string;
  emptyMessage: string;
}

export function TranscriptPanel({
  title,
  text,
  emptyMessage,
}: TranscriptPanelProps) {
  return (
    <section>
      <h2 className="text-sm font-semibold text-gray-900">
        {title}
      </h2>

      <div className="mt-2 min-h-24 rounded-lg border bg-gray-50 p-4 text-sm text-gray-700">
        {text || (
          <span className="text-gray-400">
            {emptyMessage}
          </span>
        )}
      </div>
    </section>
  );
}


