truncate table adaptive_dashboard_keywords;

alter table adaptive_dashboard_keywords AUTO_INCREMENT = 1;

CREATE TABLE `adaptive_dashboard_usertopic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `topics_id` int(11) NOT NULL,
  `content` int(11),
  PRIMARY KEY (`id`),
  KEY `adaptive_dashboard_p_topics_usertopic_idx1` (`topics_id`),
  CONSTRAINT FOREIGN KEY (`topics_id`) REFERENCES `adaptive_dashboard_topics` (`id`),
  KEY `adaptive_dashboard_user_usertopic_idx2` (`user_id`),
  CONSTRAINT FOREIGN KEY (`user_id`) REFERENCES `adaptive_dashboard_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;
