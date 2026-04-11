import { useState } from "react";
import { useEffect } from "react";
import hero from "../assets/react.svg";

// login api
import { login_service } from "../services/login";

export default function MainPageComponent() {
  const [showLogin, setShowLogin] = useState(false);
  const [username, setUsername] = useState(null)
  const [password, setPassword] = useState(null)

  function LoginButton() {
    console.log("Login button clicked.");
    setShowLogin(!showLogin);
  }
  const handleClick = async () =>{
    console.log("Send button clicked. ", username, password)
    const response = await login_service(username, password)
    console.log("Response: ", response)
  }

  return (
    // Main Div
    <div className="h-screen w-full bg-zinc-950">
      {/* Login Card General Place */}
      {showLogin && (
        <div className="flex w-full h-screen absolute z-50 items-center justify-center bg-gray-800/80">
          {/* Login Card Panel */}
          <div className="relative flex flex-col sm:h-[60%] md:h-[65%] lg:h-[55%] w-1/2 p-2 bg-white rounded-xl">
            <h1 className="text-black text-4xl font-bold text-center">Login</h1>
            <button
              onClick={LoginButton}
              className="absolute top-3 right-3 font-semibold hover:scale-110 transition-transform cursor-pointer"
            >
              Back
            </button>
            <h2 className="text-center text-lg mt-5 font-semibold">Username</h2>
            <input
              onChange={e => setUsername(e.target.value)}
              id="user-username"
              type="text"
              className="mx-auto border border-gray-300 shadow-sm rounded-md w-1/2 p-1 outline-none"
            />
            <h2 className="text-center text-lg mt-5 font-semibold">Password</h2>
            <input
            onChange={e => setPassword(e.target.value)}
              id="user-password"
              type="password"
              className="mx-auto border border-gray-300 shadow-sm rounded-md w-1/2 p-1 outline-none"
            />

            <button onClick={handleClick} className="p-2 mt-3 mx-auto w-1/3 bg-sky-500 rounded-2xl shadow-2xl hover:bg-sky-400 transition-transform cursor-pointer hover:scale-110">
              <span className="text-white font-semibold">Send</span>
            </button>
          </div>
        </div>
      )}

      {/* Header */}
      <div className="flex flex-col w-full h-[15%] p-2 items-center justify-between">
        {/* Super App Text /*/}
        <h1 className="flex text-white text-5xl font-bold mt-5 hover:scale-130 transition-transform easy-in-out duration-300">
          Super App
        </h1>
        {/* Register Login Option */}
        <div className="flex flex-row p-2 text-white mt-5">
          <button className="mx-1 cursor-pointer transition-color transition-transform duration-300 ease-in-out hover:text-red-500 hover:scale-120">
            Register{" "}
          </button>
          <span className="mx-1">/</span>

          <button
            onClick={LoginButton}
            className="mx-1 cursor-pointer transition-color transition-transform duration-300 ease-in-out hover:text-red-500 hover:scale-120"
          >
            Login
          </button>
        </div>
      </div>
      {/* Main */}
      <main className="flex w-full mt-15 justify-center">
        {/* Features Place */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 p-4 bg-white rounded-xl">
          {/* Chat Place */}
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
