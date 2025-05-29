// zoom.js

document.addEventListener("DOMContentLoaded", function () {
    const zoomableImages = document.querySelectorAll(".zoomable");

    // モーダル要素の作成
    const modal = document.createElement("div");
    modal.id = "image-modal";
    Object.assign(modal.style, {
        display: "none",
        position: "fixed",
        top: "0",
        left: "0",
        width: "100vw",
        height: "100vh",
        backgroundColor: "rgba(0,0,0,0.8)",
        justifyContent: "center",
        alignItems: "center",
        cursor: "zoom-out",
        zIndex: "1000",
        overflow: "auto"
    });

    const modalImg = document.createElement("img");
    modalImg.id = "modal-image";  // IDをつける
    Object.assign(modalImg.style, {
        maxWidth: "90%",
        maxHeight: "90%",
        userSelect: "none",
        cursor: "default"
    });

    modal.appendChild(modalImg);
    document.body.appendChild(modal);

    // モーダル背景クリックで閉じる
    modal.addEventListener("click", (e) => {
        if (e.target === modalImg) return; // 画像自体をクリックした場合は閉じない
        modal.style.display = "none";
    });

    // 画像クリックでモーダル開く
    zoomableImages.forEach(img => {
        img.style.cursor = "zoom-in";
        img.addEventListener("click", (e) => {
            e.stopPropagation();
            modalImg.src = img.src;
            modal.style.display = "flex";

            // 判定機能が読み込まれていれば実行
            if (typeof initClickGame === "function") {
                initClickGame(modalImg);
            }
        });
    });
});
