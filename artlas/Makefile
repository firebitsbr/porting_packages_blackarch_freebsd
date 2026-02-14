PORTNAME=	artlas
DISTVERSION=	154.e5fdd8d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Apache Real Time Logs Analyzer System.
WWW=		https://github.com/mthbernardes/ARTLAS

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-apache-log-parser@${PY_FLAVOR} \
		??/py-pygtail@${PY_FLAVOR} \
		??/py-telepot@${PY_FLAVOR} \
		??/py-ua-parser@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/py-user-agents@${PY_FLAVOR} \
		??/py-zabbix@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
