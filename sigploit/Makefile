PORTNAME=	sigploit
DISTVERSION=	786.0e52072
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Telecom Signaling Exploitation Framework - SS7, GTP, Diameter & SIP.
WWW=		https://github.com/SigPloiter/SigPloit

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/java-environment \
		??/py-colorama@${PY_FLAVOR} \
		??/py-configobj@${PY_FLAVOR} \
		??/py-ipy@${PY_FLAVOR} \
		??/py-pyfiglet@${PY_FLAVOR} \
		??/py-pysctp@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
