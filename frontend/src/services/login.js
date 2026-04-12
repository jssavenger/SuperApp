export async function login_service(username, password) {
    const base_api = import.meta.env.VITE_BASE_DOMAIN
    const version  = import.meta.env.VITE_VERSION
    const login_api = import.meta.env.VITE_LOGIN_API

    const API = `${base_api}${version}${login_api}`
const loginData = new URLSearchParams();
loginData.append('username', username);
loginData.append('password', password);

    try{
        const response = await fetch(API, {
            method: "POST",
            headers: {"Content-Type": "application/x-www-form-urlencoded"},
            body: loginData
        })

        const result = await response.json()
        return result
    } catch(err){
        console.log("Error from login: ", err.message)
    }
}