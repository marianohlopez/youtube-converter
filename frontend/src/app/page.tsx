"use client"

import { useState } from "react";
import axios from "axios";
import { FaMusic, FaVideo } from 'react-icons/fa';

export default function Home() {
  const [ youtubeUrlMp3, setYoutubeUrlMp3] = useState("");
  const [ youtubeUrlVideo, setYoutubeUrlVideo] = useState("");

  const handleClickMp3 = async () => {

    try { 
      const data = {
        video_url: youtubeUrlMp3,
      };
      
      await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/converter/audio`, data);
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
      
      await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/converter/video`, data);
      setYoutubeUrlVideo("");
    }
    catch (err) {
      console.log(err);
    }
  }

  return (
    <main className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-br from-pink-500 to-purple-600">
      <div className="bg-white p-8 rounded-lg shadow-lg md:w-96 w-3/4 text-center">
        <h1 className="text-2xl md:text-3xl lg:text-4xl font-semibold text-gray-800 mb-6">
          YouTube Converter
        </h1>
        <div className="mb-4">
          <input
            type="text"
            placeholder="MP3 URL"
            value={youtubeUrlMp3}
            onChange={(e) => setYoutubeUrlMp3(e.target.value)}
            className="border p-2 w-full rounded-md focus:outline-none focus:border-blue-500"
          />
        </div>
        <button
          onClick={handleClickMp3}
          className="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 w-full flex items-center justify-center transition-all duration-300"
        >
          <FaMusic className="mr-2" /> Convertir a MP3
        </button>
        <div className="my-6 border-b"></div>
        <div className="mt-4">
          <input
            type="text"
            placeholder="VIDEO URL"
            value={youtubeUrlVideo}
            onChange={(e) => setYoutubeUrlVideo(e.target.value)}
            className="border p-2 w-full rounded-md focus:outline-none focus:border-red-500"
          />
        </div>
        <button
          onClick={handleClickVideo}
          className="bg-red-500 text-white px-4 py-2 rounded-md hover:bg-red-600 w-full flex items-center justify-center transition-all duration-300 mt-4"
        >
          <FaVideo className="mr-2" /> Convertir a Video
        </button>
      </div>
    </main>
  )
}
