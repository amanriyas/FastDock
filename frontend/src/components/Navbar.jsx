

export const Navbar = () => {
    return (
        <div className="flex justify-between p-4 bg-blue-500 fixed top-0 left-0 right-0 h-20">
            <h1 className="text-5xl font-bold text-white mb-1">FastDock</h1>
            <div className="flex space-x-4 mt-2 text-white">
            <ul className="flex space-x-4">
                <li><a href="/login" className=" text-white px-4 py-2 rounded hover:scale-110 transition duration-300 font-semibold">Login</a></li>
                <li><a href="/signup" className=" text-white px-4 py-2 rounded hover:scale-110 transition duration-300 font-semibold">Sign Up</a></li>
                <li><a href="/basics" className=" text-white px-4 py-2 rounded hover:scale-110 transition duration-300 font-semibold">Docker Basics</a></li>
            </ul>
            </div>
        </div>
    );
};