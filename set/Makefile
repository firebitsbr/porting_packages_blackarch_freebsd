PORTNAME=	set
DISTVERSION=	8.0.3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Social-engineer toolkit. Aimed at penetration testing around Social-Engineering.
WWW=		https://github.com/trustedsec/social-engineer-toolkit/tags

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/impacket \
		??/java-environment \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-pefile@${PY_FLAVOR} \
		??/py-pexpect@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-qrcode@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
