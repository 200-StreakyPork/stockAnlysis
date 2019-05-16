export const formatDate = (date) => {
  let year = date.getFullYear()
  let month = '0' + (date.getMonth() + 1)
  let Date = '0' + date.getDate()
  let hour = '0' + date.getHours()
  let minute = '0' + date.getMinutes()
  let second = '0' + date.getSeconds()
  return year + '-' + month.substring(month.length - 2, month.length) + '-' + Date.substring(Date.length - 2, Date.length) + ' ' + hour.substring(hour.length - 2, hour.length) + ':' + minute.substring(minute.length - 2, minute.length) + ':' + second.substring(second.length - 2, second.length)
}
