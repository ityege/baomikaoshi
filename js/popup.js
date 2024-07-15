

// popup.js  
document.getElementById('removeButton').addEventListener('click', function () {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        var activeTab = tabs[0];
        chrome.tabs.sendMessage(activeTab.id, { action: 'removeElement' });
    });
});


document.getElementById('openPageButton1').addEventListener('click', function () {
    chrome.tabs.create({ url: 'https://miap.cc:8494/app/xcube/index.html#/login' });
});

document.getElementById('openPageButton2').addEventListener('click', function () {
    chrome.tabs.create({ url: 'https://github.com/ityege/baomikaoshi' });
});
