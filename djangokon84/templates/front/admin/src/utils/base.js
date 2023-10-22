const base = {
    get() {
        return {
            url : "http://localhost:8080/djangokon84/",
            name: "djangokon84",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "医院挂号系统"
        } 
    }
}
export default base
