"use client"

import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [ youtubeUrl, setYoutubeUrl ] = useState("");

  const handleClickMp3 = async () => {
    try { 
      const data = {video_url: youtubeUrl}
      
      await axios.post("http://127.0.0.1:8000/converter/", data, {withCredentials: true});
      setYoutubeUrl("");
    }
    catch (err) {
      console.log(err);
    }
  }

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <input type="text" 
      placeholder="URL"
      value={youtubeUrl}
      onChange={(e) => setYoutubeUrl(e.target.value)}/>
      <button onClick={handleClickMp3}>MP3</button>
    </main>
  )
}
