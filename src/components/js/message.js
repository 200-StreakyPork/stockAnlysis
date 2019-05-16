/**
 * 显示提示信息的方法。
 * @param that 显示的位置（传入this）
 * @param close 是否有关闭按钮
 * @param msg 显示的信息内容
 * @param type: success/warning/info/error
 */
export const showMsg = (that, close, msg, type) => {
  that.$message({
    showClose: close,
    message: msg,
    type: type
  })
}
/**
 * 显示消息弹框
 * @param that 显示的位置（传入this）
 * @param title 弹框标题
 * @param msg 弹框内容
 * @param type success/warning/info/error
 */
export const showMsgBox = (that, title, msg, type) => {
  that.$alert(msg, title, {
    confirmButtonText: '确定',
    type: type
  })
}
