import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from 'axios';

const Register = () => {
    const [email, setEmail] = useState("");
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();
 const handleSubmit = (evt) => {
    if (evt) {
      evt.preventDefault();
    }
    const data = {
      email: email,
      username: username,
      password: password,
    };
    axios
      .post("http://127.0.0.1:8080/register", data)
      .then((response) => {
        console.log(response);
        navigate("/")
//        alert("Register successfully");
      })
      .catch((error) => {
        alert(error);
      });
  };
    const gotoLoginPage = () => navigate("/");

    return (
        <div className='signup__container'>
            <h2>Sign up </h2>
            <form className='signup__form' onSubmit={handleSubmit}>
                <label htmlFor='email'>Email Address</label>
                <input
                    type='email'
                    name='email'
                    id='email'
                    value={email}
                    required
                    onChange={(e) => setEmail(e.target.value)}
                />
                <label htmlFor='username'>Username</label>
                <input
                    type='text'
                    id='username'
                    name='username'
                    value={username}
                    required
                    onChange={(e) => setUsername(e.target.value)}
                />
                <label htmlFor='tel'>Password</label>
                <input
                    type='password'
                    name='password'
                    id='password'
                    required
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <button className='signupBtn'>SIGN UP</button>
                <p>
                    Already have an account?{" "}
                    <span className='link' onClick={gotoLoginPage}>
                        Login
                    </span>
                </p>
            </form>
        </div>
    );
};

export default Register;