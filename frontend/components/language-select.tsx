interface LanguageOption {
  code: string;
  name: string;
}

interface LanguageSelectProps {
  label: string;
  value: string;
  options: LanguageOption[];
  onChange: (value: string) => void;
}

export function LanguageSelect({
  label,
  value,
  options,
  onChange,
}: LanguageSelectProps) {
  return (
    <label className="flex flex-col gap-2">
      <span className="text-sm font-medium text-gray-700">
        {label}
      </span>

      <select
        value={value}
        onChange={(event) => onChange(event.target.value)}
        className="rounded-lg border border-gray-300 bg-white px-3 py-2 text-sm outline-none focus:border-gray-500"
      >
        {options.map((option) => (
          <option
            key={option.code}
            value={option.code}
          >
            {option.name}
          </option>
        ))}
      </select>
    </label>
  );
}