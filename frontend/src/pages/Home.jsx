import { ChatInputBar } from "../components/ChatInputBar"
import { Navbar } from "@/components/Navbar"

export const Home = () => {
    return (
        <div className="bg-blue-300 h-screen">
            <Navbar />
            <ChatInputBar />
        </div>
    )
}