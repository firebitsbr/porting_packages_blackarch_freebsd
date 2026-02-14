PORTNAME=	hexorbase
DISTVERSION=	7
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A database application designed for administering and auditing multiple database servers simultaneously from a centralized location. It is capable of performing SQL queries and bruteforce attacks against common database servers (MySQL, SQLite, Microsoft SQL Server, Oracle, PostgreSQL).
WWW=		https://code.google.com/p/hexorbase/

LICENSE=	GPLv3 # Defaulting to GPLv3


RUN_DEPENDS=	??/mysql-python \
		??/py-psycopg2@${PY_FLAVOR} \
		??/py-pyqt4@${PY_FLAVOR} \
		??/py-qscintilla@${PY_FLAVOR} \
		??/pymssql \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
