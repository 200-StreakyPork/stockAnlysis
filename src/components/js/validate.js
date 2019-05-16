/* 是否为合法密码 6-16位仅能由大小写字母下划线数字构成 */
export function validatePassword (rule, str, callback) {
  if (!str) {
    return callback(new Error('输入不可以为空'))
  }
  setTimeout(() => {
    const passwordRegex = /^[A-Za-z0-9_]{6,16}$/
    if (!passwordRegex.test(str)) {
      callback(new Error('密码只能由6-16位大小写字母、数字以及下划线构成'))
    } else {
      callback()
    }
  }, 0)
}

/* 是否为合法用户名 6-16个小写英文及数字组成的字符 */
export function isUsername (rule, str, callback) {
  if (!str) {
    return callback(new Error('输入不可以为空'))
  }
  setTimeout(() => {
    const passwordRegex = /^.{2,12}$/
    if (!passwordRegex.test(str)) {
      callback(new Error('用户名在2-12位之间'))
    } else {
      callback()
    }
  }, 0)
}

export function isPostiveInteger (num) {
  if (!Number(num)) {
    return false
  } else {
    const passwordRegex = /^[1-9][0-9]*$/
    if (!passwordRegex.test(num)) {
      return false
    } else {
      return true
    }
  }
}
