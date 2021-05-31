function generate_url()
{
    let date = new Date();
    let year = date.getFullYear();
    let month = date.getUTCMonth()+1;
    let days = date.getUTCDate();
    let hours = date.getUTCHours()+2;
    let minutes = date.getUTCMinutes();
    let seconds = date.getUTCSeconds();
    let rest = Math.floor(Math.random()*10000)
    let url = `localhost:8000/${year}${month}${days}${hours}${minutes}${seconds}${rest}`
    alert(url);
}