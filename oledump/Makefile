PORTNAME=	oledump
DISTVERSION=	0.0.81
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Analyze OLE files (Compound File Binary Format). These files contain streams of data. This tool allows you to analyze these streams.
WWW=		http://blog.didierstevens.com/programs/oledump-py/

LICENSE=	GPLv3 # Defaulting to GPLv3


RUN_DEPENDS=	??/py-lxml@${PY_FLAVOR} \
		??/py-olefile@${PY_FLAVOR} \
		??/py-yara-dex@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
