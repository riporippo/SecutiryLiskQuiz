document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("image-modal");
  const modalImg = document.getElementById("modal-image");
  const resultBox = document.getElementById("result-message");

  if (!modal || !modalImg || !resultBox) return;

  // 正解スポット（元画像サイズ基準）
  
  function isInRect(x, y, rect) {
  return x >= rect.x && x <= rect.x + rect.width && y >= rect.y && y <= rect.y + rect.height;
}

const correctRects = [
  { x: 150, y: 50, width: 350, height: 55 },  // x:250-600, y:50-100の矩形
];

  modalImg.addEventListener("click", (e) => {
    e.stopPropagation();

    const rect = modalImg.getBoundingClientRect();

    // 表示画像上の相対位置
    const clickX = e.clientX - rect.left;
    const clickY = e.clientY - rect.top;

    // スケール変換（表示サイズ → 元サイズ）
    const scaleX = modalImg.naturalWidth / rect.width;
    const scaleY = modalImg.naturalHeight / rect.height;

    const imageX = clickX * scaleX;
    const imageY = clickY * scaleY;

    // 判定
      let found = false;
  for (const rect of correctRects) {
    if (isInRect(imageX, imageY, rect)) {
      found = true;
      break;
    }
  }

    // 表示するマーク（○か×）と色
    const mark = found ? "○" : "×";
    const color = found ? "green" : "red";
    resultBox.textContent = found ? "正解！" : "不正解...";
    resultBox.style.color = color;

    // 表示用マークを追加（モーダル内に）
    showMark(e.clientX, e.clientY, mark, color);
  });

  // マーク表示関数（画面座標から絶対配置）
  function showMark(clientX, clientY, symbol, color) {
    const mark = document.createElement("div");
    mark.textContent = symbol;

    // 画面全体に対して絶対位置に配置（fixed）
    Object.assign(mark.style, {
      position: "fixed",
      left: `${clientX}px`,
      top: `${clientY}px`,
      transform: "translate(-50%, -50%)",
      color: color,
      fontSize: "32px",
      fontWeight: "bold",
      pointerEvents: "none",
      zIndex: "2000"
    });

    document.body.appendChild(mark);

    setTimeout(() => {
      mark.remove();
    }, 1000);
  }
});
