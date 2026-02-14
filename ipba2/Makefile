PORTNAME=	ipba2
DISTVERSION=	95.c03bd85
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	IOS Backup Analyzer.
WWW=		http://www.ipbackupanalyzer.com/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-pillow@${PY_FLAVOR} \
		??/py-pyside@${PY_FLAVOR} \
		??/qt4 \
		devel/py-six@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
