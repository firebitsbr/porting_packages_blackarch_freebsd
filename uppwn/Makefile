PORTNAME=	uppwn
DISTVERSION=	9.f69dec4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A script that automates detection of security flaws on websites file upload systems.
WWW=		https://github.com/ferrery1/UpPwn

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/phantomjs \
		??/py-pymiproxy@${PY_FLAVOR} \
		??/py-selenium@${PY_FLAVOR} \
		??/py-xvfbwrapper@${PY_FLAVOR} \
		??/xorg-server-xvfb \
		lang/python3 \
		www/node


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
