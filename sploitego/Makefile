PORTNAME=	sploitego
DISTVERSION=	153.d9568dc
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Maltego Penetration Testing Transforms.
WWW=		https://github.com/allfro/sploitego

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/amap \
		??/metasploit \
		??/p0f \
		lang/python3 \
		security/nmap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
