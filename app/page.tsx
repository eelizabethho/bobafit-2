import SearchBar from "./components/SearchBar";

export default function Home() {
  return (
    <div 
    className="min-h-screen flex items-center justify-center bg-white text-black dark:bg-black dark:text-white"
      style={
          { backgroundImage: 'url("/bobabackground.jpg")', 
            backgroundRepeat: 'no-repeat', 
            backgroundSize: 'cover',
            backgroundPosition: 'center',
            
          }}
    >
      {/* Square Box Component */}
      <div className="w-150 h-150 rounded-2xl shadow-lg backdrop-blur flex flex-col items-center justify-start">
        <div className="w-full flex items-center justify-between pt-16 px-8 pb-8">
          <div className="w-10"></div>
          <h1 className="text-black text-4xl text-center">ボンバフィット</h1>
          <img 
            src="/AmazonLogo.png"
            alt="Amazon Logo"
            className="w-15 h-12 "
            />
        </div>
        {/* Search Bar */}
        <div className="flex flex-col items-center">
          <SearchBar />
        </div>
      </div>


    </div>
  );
}
