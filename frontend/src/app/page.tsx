"use client"

import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [ youtubeUrlMp3, setYoutubeUrlMp3] = useState("");
  const [ youtubeUrlVideo, setYoutubeUrlVideo] = useState("");

  const handleClickMp3 = async () => {
    try { 
      const data = {
        video_url: youtubeUrlMp3,
      };
      
      await axios.post("http://127.0.0.1:8000/converter/audio", data);
      setYoutubeUrlMp3("");
    }
    catch (err) {
      console.log(err);
    }
  }

  const handleClickVideo = async () => {
    try { 
      const data = {
        video_url: youtubeUrlVideo,
      };
      
      await axios.post("http://127.0.0.1:8000/converter/video", data);
      setYoutubeUrlVideo("");
    }
    catch (err) {
      console.log(err);
    }
  }

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <input type="text" 
      placeholder="MP3 URL"
      value={youtubeUrlMp3}
      onChange={(e) => setYoutubeUrlMp3(e.target.value)}/>
      <button onClick={handleClickMp3}>MP3</button>
      <input type="text" 
      placeholder="VIDEO URL"
      value={youtubeUrlVideo}
      onChange={(e) => setYoutubeUrlVideo(e.target.value)}/>
      <button onClick={handleClickVideo}>VIDEO</button>
    </main>
  )
}
