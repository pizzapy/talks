/**
 * Basic notification class
 */
function Notification(msg, type) {
  this.msg = msg;
  this.type = typeof type !== 'undefined' ? type : 'success';
}

Notification.prototype.show = function() {
  // build notification
  var notif = document.createElement('div');
  notif.id = 'notification';
  notif.className = this.type;
  notif.innerHTML = this.msg;

  // prepend notificaiton
  var doc = document.getElementsByTagName("body")[0];
  doc.insertBefore(notif, doc.firstChild);
};