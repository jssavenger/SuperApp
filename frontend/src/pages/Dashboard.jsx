import { useEffect, useEffectEvent, useState } from "react";
import { useLocation } from "react-router-dom";
import AlertComponent from "../components/AletsComp";

export default function AdminDashboardPage() {
  const location = useLocation();
  const [showAlert, setShowAlert] = useState(true);
  const [showMenu, setShowMenu] = useState(true);

  const handleClick = async () => {
    setShowMenu(!showMenu);
  };

  useEffect(() => {
    if (location.state?.showAlertFirst) {
      setShowAlert(true);

      window.history.replaceState({}, document.title);
    }
  }, [location]);

  return (
    <div className="flex h-screen w-full bg-gray-100">
      {showAlert && (
        <AlertComponent
          icon={"correct"}
          head={location.state.message}
          subject={"Login Successful"}
          onClose={() => setShowAlert(false)}
        />
      )}
      {showMenu && (
        <div className="flex flex-col absolute z-120 h-screen w-1/5 bg-zinc-800 justify-start rounded-r-xl">
          <h2 className="text-center text-white mt-1 mb-1">Smart Navigator</h2>
          <hr />
          <div className="flex flex-col w-full bg-white h-auto max-h-1/2 text-center ">
            <div className="w-full h-auto bg-gray-200 hover:text-black hover:bg-white transition-color duration-300">
              <span>Chat</span>
            </div>
            <div className="w-full h-auto bg-gray-200 hover:text-black hover:bg-white transition-color duration-300">
              <span>Social</span>
            </div>
            <div className="w-full h-auto bg-gray-200 hover:text-black hover:bg-white transition-color duration-300">
              <span>Games</span>
            </div>
            <div className="w-full h-auto bg-gray-200 hover:text-black hover:bg-white transition-color duration-300">
              <span>AI</span>
            </div>
          </div>
          <div className="flex flex-col max-h-1/4 h-1/3 w-full bg-zinc-700 mt-auto">
            <h3 className="text-center text-white mt-1 mb-1">User Info</h3>
            <hr />
            <div className="w-full h-auto bg-gray-200 hover:text-black hover:bg-white transition-color duration-300 text-center">
              <span className="font-semibold">Username: </span>
              <span>{location.state.username}</span>
            </div>
          </div>
        </div>
      )}
      <div className="flex flex-col h-screen w-full bg-zinc-950 ">
        <div className="h-[10%] w-full bg-zinc-1000">
          <h1 className="text-white text-center text-4xl font-semibold">
            Smart Dashboard
          </h1>
        </div>
      </div>
    </div>
  );
}
