chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action === 'removeElement') {

        //题库先使用python处理成json格式,javascript擅长处理成json格式数据
        const configUrl = chrome.runtime.getURL('resources/config.json');
        fetch(configUrl).then(response => { return response.json() })
            .then(data => {

                // 假设你有一个iframe的id是'myIframe'  
                var iframe = document.getElementsByTagName('iframe');
                var iframeDocument = iframe[0].contentDocument || iframe[0].contentWindow.document;

                const cardBodies = iframeDocument.getElementsByClassName("el-card__body");
                // console.log(cardBodies);

                for (let child of cardBodies[0].children) {
                    // console.log("child:"+child);
                    pre = child.getElementsByTagName("pre");
                    // console.log(pre[0].textContent);
                    for (let t of data) {
                        if (pre[0].textContent.replace(/[^\u4e00-\u9fa5]/g, '') === (t.题目)) {
                            // console.log(t.标准答案);
                            if (t.标准答案 === "A") {
                                child.getElementsByTagName("label")[0].click();
                            } else if (t.标准答案 === "B") {
                                child.getElementsByTagName("label")[1].click();
                            } else if (t.标准答案 === "C") {
                                child.getElementsByTagName("label")[2].click();
                            } else if (t.标准答案 === "D") {
                                child.getElementsByTagName("label")[3].click();
                            }

                            break;
                        }

                    }

                }

            });

    }
});
