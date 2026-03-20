import hero from "../assets/react.svg";

export default function MainPageComponent() {
  return (
    // Main Div
    <div className="h-screen w-full bg-zinc-950">
      {/* Header */}
      <div className="flex flex-col w-full h-[15%] p-2 items-center justify-between">
        {/* Super App Text /*/}
        <h1 className="flex text-white text-5xl font-bold mt-5 hover:scale-130 transition-transform easy-in-out duration-300">
          Super App
        </h1>
        {/* Register Login Option */}
        <div className="flex flex-row p-2 text-white mt-5">
          <span className="mx-1 cursor-pointer transition-color transition-transform duration-300 ease-in-out hover:text-red-500 hover:scale-120">
            Register{" "}
          </span>
          <span className="mx-1">/</span>
          <span className="mx-1 cursor-pointer transition-color transition-transform duration-300 ease-in-out hover:text-red-500 hover:scale-120">
            Login
          </span>
        </div>
      </div>
      {/* Main */}
      <main className="flex w-full mt-10 justify-center">
        {/* Features Place */}
        <div className="grid grid-cols-1 sm:grid-cols-3 lg:grid-cols-4 gap-4 p-4 bg-white rounded-xl">
          <div className="flex flex-col items-center justify-center">
            <div className="flex">
              <img src={hero} alt="" />
            </div>
            <span className="mt-1 font-semibold hover:scale-110 transition-transform easy-in-out duration-300">
              Chat
            </span>
          </div>
          {/* Social Media */}
          <div className="flex flex-col items-center justify-center">
            <div className="flex">
              <img src={hero} alt="" />
            </div>
            <span className="mt-1 font-semibold hover:scale-110 transition-transform easy-in-out duration-300">
              Social Media
            </span>
          </div>
          {/* AI */}
          <div className="flex flex-col items-center justify-center">
            <div className="flex">
              <img src={hero} alt="" />
            </div>
            <span className="mt-1 font-semibold hover:scale-110 transition-transform easy-in-out duration-300">
              AI
            </span>
          </div>
        </div>
      </main>
    </div>
  );
}
