import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import Cookies from "js-cookie";
import axios from "axios";

const Login = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [qrCodeUrl, setQrCodeUrl] = useState('');
    const navigate = useNavigate();

   const handleSubmit = async (evt) => {
    if (evt) {
      evt.preventDefault();
    }
    const data = {
      email: email,
      password: password,
    };
    const news = async () => {
      let res = await axios
        .post("http://127.0.0.1:8080/token", data)
        .then((response) => {
          console.log(response);
          Cookies.set("token", response.data.access_token);
//          return response;
        })

        .catch((error) => {
          console.log(error.message);
        });
      return res;
    };

    let x = await news();
    if (x) {
      window.location.reload();
    }
  };

    const gotoSignUpPage = () => navigate("/register");

    return (
        <div className='login__container'>
            <h2>Login </h2>
            <form className='login__form' onSubmit={handleSubmit}>
                <label htmlFor='email'>Email</label>
                <input
                    type='text'
                    id='email'
                    name='email'
                    value={email}
                    required
                    onChange={(e) => setEmail(e.target.value)}
                />
                <label htmlFor='password'>Password</label>
                <input
                    type='password'
                    name='password'
                    id='password'
                    required
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <button className='loginBtn'>SIGN IN</button>
                <p>
                    Don't have an account?{" "}
                    <span className='link' onClick={gotoSignUpPage}>
                        Sign up
                    </span>
                </p>
            </form>
        </div>
    );
};

export default Login;