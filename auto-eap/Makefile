PORTNAME=	auto-eap
DISTVERSION=	18.ee36d37
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Automated Brute-Force Login Attacks Against EAP Networks.
WWW=		https://github.com/Tylous/Auto_EAP

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/wpa_supplicant \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
