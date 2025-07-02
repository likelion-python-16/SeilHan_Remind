// 공통요소로 처리예정
function datetimeToString(datetime){
    if (!datetime) return "-";
    const date = new Date(datetime);
    return date.toLocaleString("ko-KR", { timeZone: "Asia/Seoul" });
}