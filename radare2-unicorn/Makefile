PORTNAME=	radare2-unicorn
DISTVERSION=	921.430b6fa
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Unicorn Emulator Plugin for radare2.
WWW=		https://github.com/radare/radare2-extras/tree/master/unicorn

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/pkg-config \
		devel/git

RUN_DEPENDS=	??/capstone \
		??/jansson \
		??/radare2 \
		??/unicorn \
		??/yara \
		security/openssl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
