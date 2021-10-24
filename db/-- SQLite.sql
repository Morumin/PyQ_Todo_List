-- SQLite

CREATE TABLE todo(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	duedate TEXT,
    status TEXT,
    memo TEXT
);

INSERT INTO todo (name, duedate, status, memo) 
VALUES("メールを書く","2017-10-10","未完了","佐藤様に次回の打ち合わせの件を連絡"),
      ("資料作成","2017-10-20","未完了","’’"),
      ("バグを修正","2017-10-30","未完了","仕様の解釈ミスでした")