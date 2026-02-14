PORTNAME=	cloudmare
DISTVERSION=	108.9c5a39f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A simple tool to find origin servers of websites protected by CloudFlare with a misconfiguration DNS.
WWW=		https://github.com/MrH0wl/Cloudmare

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/dos2unix \
		devel/git

RUN_DEPENDS=	??/py-backoff@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-certifi@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
