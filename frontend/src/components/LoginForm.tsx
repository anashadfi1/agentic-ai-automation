import React from 'react'
import { useState } from 'react'

const LoginForm = () => {

    const [username, setUsername] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")

    const [errors, setErrors] = useState <{email: string, password: string}>(
        {
        email:"",
        password:""
    }
    )

     const handleSubmit = (e: React.SyntheticEvent<HTMLFormElement>) => {
    e.preventDefault();

    setErrors({ email: "", password: "" });

    if (!email.includes("@")) {
        setErrors({ email: "email must include @", password: "" });
        return;
    }

    if (password.length < 6) {
        setErrors({ email: "", password: "password must be more than 6 characters" });
    }
};
  return (
    <form className="flex justify-center w-full max-w-md flex-col gap-5 rounded-2xl bg-white p-8 shadow-xl" onSubmit={handleSubmit} > 
    <div className="mb-2"> <h2 className="text-2xl font-bold text-gray-900">Welcome back</h2>
     <p className="mt-1 text-sm text-gray-500"> Sign in to continue to your account </p>
     </div> 
     <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} 
     className="w-full rounded-lg border border-gray-300 px-4 py-3 text-gray-900 
     outline-none transition placeholder:text-gray-400 focus:border-blue-500 
     focus:ring-2 focus:ring-blue-200" /> 
      <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} className="w-full rounded-lg 
      border border-gray-300 px-4 py-3 
      text-gray-900 outline-none transition placeholder:text-gray-400 
      focus:border-blue-500 focus:ring-2 focus:ring-blue-200" /> 
      <button type="submit" className="mt-2 w-full rounded-lg 
      bg-blue-600 px-4 py-3 font-semibold text-white transition 
      hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 
      focus:ring-offset-2 active:scale-[0.98]" > Submit </button> 
      </form>
      )
}

export default LoginForm
