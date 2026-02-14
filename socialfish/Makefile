PORTNAME=	socialfish
DISTVERSION=	250.a22b58d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Ultimate phishing tool with Ngrok integrated.
WWW=		https://github.com/UndeadSec/SocialFish

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-flask-login@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-huepy@${PY_FLAVOR} \
		??/py-nmap@${PY_FLAVOR} \
		??/py-pylatex@${PY_FLAVOR} \
		??/py-qrcode@${PY_FLAVOR} \
		??/py-wget@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
