

export const Navbar = () => {
    return (
        <div className="flex justify-between p-4 bg-blue-500 fixed top-0 left-0 right-0">
            <h1 className="text-2xl font-bold text-white">FastDock</h1>
            <div className="flex space-x-4 mt-4 text-white">
            <ul className="flex space-x-4">
                <li><a href="/login" className="px-4 py-2 rounded hover:scale-110 transition duration-300">Login</a></li>
                <li><a href="/signup" className="px-4 py-2 rounded hover:scale-110 transition duration-300">Sign Up</a></li>
                <li><a href="/basics" className="px-4 py-2 rounded hover:scale-110 transition duration-300">Docker Basics</a></li>
            </ul>
            </div>
        </div>
    );
};