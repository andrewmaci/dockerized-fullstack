import React from "react";
import UserInterface from "@/components/UserInterface";

const Home:React.FC= ()=>{
  return(
    <div className="flex justify-center">
      <UserInterface backendName="flask"/>
    </div>
  );
}

export default Home