CREATE DATABASE IF NOT EXISTS test2 CHARACTER SET 'utf8';
SHOW DATABASES;
USE test2;
DROP TABLE IF EXISTS test2.students;	-- 如果存在学生表，则把学生表删除

-- 创建学生表
CREATE TABLE test2.students(
sid CHAR(7) UNIQUE,
sname VARCHAR(30),
ssex CHAR(2),
sphone CHAR(11),
sage INT(3),
did VARCHAR(3)
);

-- 插入数据
INSERT INTO test2.students VALUES('s000001','焦元','男','17629299956','18','d01');

#1、创建存储过程：往学生表中插入学生
DELIMITER $$
CREATE PROCEDURE insert_student(IN st_count INT)
BEGIN
	DECLARE sid_max VARCHAR(7);   #存查询到的最大的sid
	DECLARE insert_sid VARCHAR(7);
	DECLARE xing VARCHAR(500) DEFAULT '赵钱孙李周吴郑王冯陈诸卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮齐康伍余元卜顾孟平黄和穆萧尹姚邵堪汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董粱杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯咎管卢莫经房裘干解应宗丁宣贲邓郁单杭洪包诸左石崔吉钮龚';
	DECLARE ming VARCHAR(500) DEFAULT '明国华建文平志伟东海强晓生光林小民永杰军金健一忠洪江福祥中正振勇耀春大宁亮宇兴宝少剑云学仁涛瑞飞鹏安亚泽世汉达卫利胜敏群波成荣新峰刚家龙德庆斌辉良玉俊立浩天宏子松克清长嘉红山贤阳乐锋智青跃元武广思雄锦威启昌铭维义宗英凯鸿森超坚旭政传康继翔栋仲权奇礼楠炜友年震鑫雷兵万星骏伦绍麟雨行才希彦兆贵源有景升惠臣慧开章润高佳虎根远力进泉茂毅富博霖顺信凡豪树和恩向道川彬柏磊敬书鸣芳培全炳基冠晖京欣廷哲保秋君劲轩帆若连勋祖锡吉崇钧田石奕发洲彪钢运伯满庭申湘皓承梓雪孟其潮冰怀鲁裕翰征谦航士尧标洁城寿枫革纯风化逸腾岳银鹤琳显焕来心凤睿勤延凌昊西羽百捷定琦圣佩麒虹如靖日咏会久昕黎桂玮燕可越彤雁孝宪萌颖艺夏桐月瑜沛诚夫声冬奎扬双坤镇楚水铁喜之迪泰方同滨邦先聪朝善非恒晋汝丹为晨乃秀岩辰洋然厚灿卓杨钰兰怡灵淇美琪亦晶舒菁真涵爽雅爱依静棋宜男蔚芝菲露娜珊雯淑曼萍珠诗璇琴素梅玲蕾艳紫珍丽仪梦倩伊茜妍碧芬儿岚婷菊妮媛莲娟';
	DECLARE insert_name VARCHAR(30);
	DECLARE insert_sex CHAR(2);
	DECLARE insert_sphone VARCHAR(11);
	DECLARE insert_age INT;
	DECLARE insert_did VARCHAR(3);
	
	WHILE st_count > 0 DO
		
		#1、将查到的最大的sid的值赋值给sid_max
		SELECT MAX(sid) INTO sid_max FROM students;
			#处理查到的最大值，给最大值+1
		SET insert_sid = CONCAT('s',LPAD(SUBSTR(sid_max,2)+1,6,'0'));
		
		#2、构造姓名
		SET insert_name =CONCAT(SUBSTR(xing,CEIL(RAND()*CHAR_LENGTH(xing)),1),SUBSTR(ming,CEIL(RAND()*CHAR_LENGTH(ming)),1),SUBSTR(ming,CEIL(RAND()*CHAR_LENGTH(ming)),1));
		
		#3、随机生成性别
		IF CEIL(RAND()*2) > 1 THEN SET insert_sex='男';
				      ELSE SET insert_sex='女';
		END IF;
		
		#4、随机生成电话号码
		SET insert_sphone = CONCAT('13',LPAD(ROUND(RAND()*1000000000),9,'0'));
		
		#5、生成学生的年龄，年龄在20~30
		SET insert_age = ROUND((RAND()+2)*10);
		
		#6、随机生成学生所在系
		CASE CEIL(RAND()*3) WHEN 1 THEN SET insert_did='d01';
		                    WHEN 2 THEN SET insert_did='d02';
		                    ELSE SET insert_did='d03';
		END CASE;
		
		SET st_count = st_count - 1;
		INSERT INTO test2.students VALUES(insert_sid,insert_name,insert_sex,insert_sphone,insert_age,insert_did);
	END WHILE;
END $$
DELIMITER ;

CALL insert_student(500000);