export default function SearchBar() {
  return (
    <form className="flex items-center max-w-lg w-full space-x-2">   
      <div className="relative w-full">
        {/* Icon Magify Glass */}
        <div className="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
          <svg
            className="w-5 h-5 text-gray-500"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="m21 21-3.5-3.5M17 10a7 7 0 1 1-14 0 7 7 0 0 1 14 0Z"
            />
          </svg>
        </div>
        <input
          type="text"
          className="block w-full pl-10 pr-3 py-2.5 bg-white/70 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 placeholder-gray-500 shadow-sm"
          placeholder="type food item"
          required
        />
      </div>

      <button
        type="submit"
        className="inline-flex items-center text-white bg-blue-600 hover:bg-blue-700 focus:ring-4 focus:ring-blue-300 shadow font-medium text-sm px-4 py-2 rounded-lg"
      >
        Search
      </button>
    </form>
  );
}
